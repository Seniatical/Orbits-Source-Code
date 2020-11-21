import discord
from discord.ext import commands
import json
import random
from discord.ext.commands.cooldowns import BucketType

mainshop = [{"name":"Cookie","price":100,"description":"There Is No Description For A Cookie Smh"},
                {"name":"Fish","price":200,"description":"Don't You Love The Smell"},
                {"name":"Koolaid","price":300,"description":"Cool Now You Got A Koolaid"},
                {"name":"Laptop","price":1000,"description":"Good Job Now You Can Play Tetris"},
                {"name":"Pc","price":10000,"description":"If You Have This All Hail The King :crown:"}]

async def open_account(user):

        users = await get_bank_data()

        if str(user.id) in users:
            return False
        else:
            users[str(user.id)] = {}
            users[str(user.id)]["wallet"] = 0
            users[str(user.id)]["bank"] = 0

        with open("bank.json", "w") as f:
            json.dump(users, f)
        return True

async def get_bank_data():
    with open("bank.json", "r") as f:
        users = json.load(f)

        return users

async def update_bank(user,change = 0,mode = "wallet"):
    users = await get_bank_data()

    users[str(user.id)][mode] += change

    with open("bank.json", "w") as f:
        json.dump(users, f)

    bal = users[str(user.id)]["wallet"],users[str(user.id)]["bank"]
    return bal

async def get_item_data():
    with open("mainbank.json", "r") as f:
        users = json.load(f)

    return users

async def buy_this(user,item_name,amount):
    item_name = item_name.lower()
    name_ = None
    for item in mainshop:
        name = item["name"].lower()
        if name == item_name:
            name_ = name
            price = item["price"]
            break

    if name_ == None:
        return [False,1]

    cost = price*amount

    users = await get_bank_data()

    bal = await update_bank(user)

    if bal[0]<cost:
        return [False,2]


    try:
        index = 0
        t = None
        for thing in users[str(user.id)]["bag"]:
            n = thing["item"]
            if n == item_name:
                old_amt = thing["amount"]
                new_amt = old_amt + amount
                users[str(user.id)]["bag"][index]["amount"] = new_amt
                t = 1
                break
            index+=1 
        if t == None:
            obj = {"item":item_name , "amount" : amount}
            users[str(user.id)]["bag"].append(obj)
    except:
        obj = {"item":item_name , "amount" : amount}
        users[str(user.id)]["bag"] = [obj]        

    with open("mainbank.json","w") as f:
        json.dump(users,f)

    await update_bank(user,cost*-1,"wallet")

    return [True,"Worked"]

async def sell_this(user,item_name,amount,price = None):
        item_name = item_name.lower()
        name_ = None
        for item in mainshop:
            name = item["name"].lower()
            if name == item_name:
                name_ = name
                if price==None:
                    price = 0.9* item["price"]
                break

        if name_ == None:
            return [False,1]

        cost = price*amount

        users = await get_bank_data(user)

        bal = await update_bank(user) 


        try:
            index = 0
            t = None
            for thing in users[str(user.id)]["bag"]:
                n = thing["item"]
                if n == item_name:
                    old_amt = thing["amount"]
                    new_amt = old_amt - amount
                    if new_amt < 0:
                        return [False,2]
                    users[str(user.id)]["bag"][index]["amount"] = new_amt
                    t = 1
                break
            index+=1 
            if t == None:
                return [False,3]
        except:
            return [False,3]    

        with open("mainbank.json","w") as f:
            json.dump(users,f)

        await update_bank(user,cost,"wallet")

        return [True,"Worked"]


class ECO(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
      

    @commands.command(aliases = ["bal"])
    async def balance(self, ctx, member : discord.Member = None):
        member = ctx.author if not member else member
        await open_account(member)
        user = member
        users = await get_bank_data()
        wallet_amt = users[str(user.id)]["wallet"]
        bank_amt = users[str(user.id)]["bank"]
        em = discord.Embed(title = f"{member.name}`s balance",color = 0xFFC0CB)
        em.add_field(name = "Wallet balance", value = wallet_amt)
        em.add_field(name = "Bank balance", value = bank_amt)
        await ctx.send(embed = em)


    @commands.command()
    @commands.cooldown(1,30, commands.BucketType.user)
    async def beg(self, ctx):
        await open_account(ctx.author)

        users = await get_bank_data()

        user = ctx.author

        earnings = random.randrange(150)


        await ctx.send(f"Someone Gave You {earnings} coins!")


        users[str(user.id)]["wallet"] += earnings

        with open("bank.json", "w") as f:
            json.dump(users,f )
            return


    @commands.command(aliases = ["w"])
    async def withdraw(self,ctx,amount = None):
        await open_account(ctx.author)

        if amount == None:
            await ctx.send("That's Not A Number smh")
            return

        bal = await update_bank(ctx.author)

        amount = int(amount)
        if amount>bal[1]:
            await ctx.send("Bank's Only For Rich People")
            return
        if amount<0:
            await ctx.send("You Adding Negative Moneys???")
            return

        await update_bank(ctx.author,amount,)
        await update_bank(ctx.author,-1*amount,"bank")

        await ctx.send(f"You Withdrew {amount} Coins!")


    @commands.command(aliases = ["d"])
    async def deposit(self,ctx,amount = None):
        await open_account(ctx.author)

        if amount == None:
            await ctx.send("That's Not A Number smh")
            return

        bal = await update_bank(ctx.author)

        amount = int(amount)
        if amount>bal[0]:
            await ctx.send("Bank's Only For Rich People")
            return
        if amount<0:
            await ctx.send("You Adding Negative Moneys???")
            return

        await update_bank(ctx.author,-1*amount,)
        await update_bank(ctx.author,amount,"bank")

        await ctx.send(f"You Deposited {amount} Coins!")


    @commands.command()
    async def send(self,ctx,member:discord.Member,amount = None):
        await open_account(ctx.author)
        await open_account(member)

        if amount == None:
            await ctx.send("That's Not A Number smh")
            return

        bal = await update_bank(ctx.author)
        if amount == "all":
            amount = bal[0]

        bal = await update_bank(ctx.author)

        amount = int(amount)
        if amount>bal[1]:
            await ctx.send("Bank's Only For Rich People")
        if amount<0:
            await ctx.send("You Adding Negative Moneys???")

        await update_bank(ctx.author,-1*amount,"bank")
        await update_bank(member,amount,"bank")

        await ctx.send(f"You Sent {amount} Coins!")


    @commands.command()
    async def rob(self,ctx,member:discord.Member,amount = None):
        await open_account(ctx.author)
        await open_account(member)


        bal = await update_bank(member)

        earnings = random.randrange(-500, 1000)
        if bal[0]<500:
            await ctx.send(f"{member} Has Less Than 500 Coins They Are Not Worth It")
            return

        amount = int(amount)


        await update_bank(ctx.author,earnings)
        await update_bank(member,-1*earnings)

        await ctx.send(f"You Robbed {earnings} Coins!")


    @commands.command()
    async def slots(self,ctx,amount = None):
        if amount == None:
            await ctx.send("That's Not A Number smh")
            return

        bal = await update_bank(ctx.author)

        amount = int(amount)
        if amount>bal[1]:
            await ctx.send("Bank's Only For Rich People")
            return
        if amount<0:
            await ctx.send("You Adding Negative Moneys???")
            return

        final = []
        for i in range(3):
            a = random.choice([':red_circle:',':blue_circle:',':green_circle:'])

            final.append(a)

        await ctx.send(str(final))

        if final[0] == final[1] or final[0] == final[2] or final[2] == final[1]:
            await update_bank(ctx.author,2*amount,"bank")
            await ctx.send("You Won!")
        else:
            await update_bank(ctx.author,-1*amount,"bank")
            await ctx.send("Git Gud Kid")


    @commands.command()
    async def shop(self,ctx):
        em = discord.Embed(title = "Shop")

        for item in mainshop:
            name = item["name"]
            price = item["price"]
            desc = item["description"]
            em.add_field(name = name, value = f"${price} | {desc}")

        await ctx.send(embed = em)



    @commands.command()
    async def buy(self,ctx,item,amount = 1):
        await open_account(ctx.author)

        res = await buy_this(ctx.author,item,amount)

        if not res[0]:
            if res[1]==1:
                await ctx.send("That Object isn't there!")
                return
            if res[1]==2:
                await ctx.send(f"You don't have enough money in your wallet to buy {amount} {item}")
                return


        await ctx.send(f"You just bought {amount} {item}")


    @commands.command(aliases = ["inv"])
    async def inventory(self,ctx):
        await open_account(ctx.author)
        user = ctx.author
        users = await get_item_data()

        try:
            bag = users[str(user.id)]["bag"]
        except:
            bag = []


        em = discord.Embed(title="Inventory")

        for item in bag:
            name = item["item"]
            amount = item["amount"]

            em.add_field(name = name, value = amount)    

        await ctx.send(embed = em)


    @commands.command()
    async def sell(self,ctx,item,amount = 1):
        await open_account(ctx.author)

        res = await sell_this(ctx.author,item,amount)

        if not res[0]:
            if res[1]==1:
                await ctx.send("That Object isn't there!")
                return
            if res[1]==2:
                await ctx.send(f"You don't have {amount} {item} in your bag.")
                return
            if res[1]==3:
                await ctx.send(f"You don't have {item} in your bag.")
                return

        await ctx.send(f"You just sold {amount} {item}.")

    @commands.command(aliases = ["lb"])
    async def leaderboard(self,ctx,x = 5):
        users = await get_bank_data()
        leader_board = {}
        total = []
        for user in users:
            name = int(user)
            total_amount = users[user]["wallet"] + users[user]["bank"]
            leader_board[total_amount] = name
            total.append(total_amount)

        total = sorted(total,reverse=True)    

        em = discord.Embed(title = f"Top {x} Richest People" , description = "Richest Player Check",color = discord.Color(0xfa43ee))
        index = 1
        for amt in total:
            id_ = leader_board[amt]
            member = ctx.get_user(id_)
            name = member.name
            em.add_field(name = f"{index}. {name}" , value = f"{amt}",  inline = False)
            if index == x:
                break
            else:
                index += 1

        await ctx.send(embed = em)


    @commands.Cog.listener()
    async def on_command_error(self,ctx,error):
        if isinstance(error,commands.MissingPermissions):
            await ctx.send("You Can't Do That ;-;")
            await ctx.message.delete()
        elif isinstance(error,commands.CommandNotFound):
            await ctx.send("That's Not A Command Sily")
        elif isinstance(error,commands.MissingRequiredArgument):
            await ctx.send("Please Enter All The Args")
        elif isinstance(error, commands.CommandOnCooldown):
            msg = '**Still on cooldown**, please try again in {:.2f}s'.format(error.retry_after)
            await ctx.send(msg)
        else:
            raise error


def setup(bot):
    bot.add_cog(ECO(bot))
