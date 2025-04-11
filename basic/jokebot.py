import random

class JokeBot:
    def __init__(self):
        self.jokes = [
            "Why don't skeletons fight each other?\nThey don't have the guts! 💀😂",
            "Why don't scientists trust atoms?\nBecause they make up everything! 😄",
            "Why did the computer go to the doctor?\nBecause it had a virus! 💻🤒"
        ]

    def tell_joke(self):
        return random.choice(self.jokes)

def main():
    print("🤖 JokeBot se milo! Type 'joke' ek chutkula sunne ke liye, ya 'exit' band karne ke liye.")
    bot = JokeBot()
    while True:
        user_input = input("Aap: ").strip().lower()
        if user_input == 'joke':
            print("JokeBot:", bot.tell_joke())
        elif user_input == 'exit':
            print("JokeBot: Achha chalo, baad mein milte hain! 😂")
            break
        else:
            print("JokeBot: Mujhe sirf 'joke' ya 'exit' samajh aata hai bhai!")

if __name__ == "__main__":
    main()




   # 🧠 Isko Samajhne ka Tareeqa:
#JokeBot class: Yeh ek machine jaisi soch hai jisme chutkule store hain.

#tell_joke method: Jab bhi user bole ‘joke’, yeh ek random joke return karta hai.

#main() function: Yeh program ka boss hai — yeh user se baat karta hai aur decide karta hai kya dikhana hai.

#Input/Output: User type karega "joke" ya "exit", aur JokeBot accordingly react karega.


