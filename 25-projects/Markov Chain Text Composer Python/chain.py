import streamlit as st
import random
import re
from collections import defaultdict

# Function to build a Markov chain model
def build_markov_chain(text, order=5):
    words = re.findall(r'\b\w+\b', text)
    markov_dict = defaultdict(list)
    
    for i in range(len(words) - order):
        key = tuple(words[i:i+order])
        markov_dict[key].append(words[i+order])
    
    return markov_dict

# Function to generate text
def generate_text(markov_dict, num_words=50, order=2):
    start_key = random.choice(list(markov_dict.keys()))
    generated_words = list(start_key)
    
    for _ in range(num_words - order):
        key = tuple(generated_words[-order:])
        if key in markov_dict:
            generated_words.append(random.choice(markov_dict[key]))
        else:
            break
    
    return ' '.join(generated_words)

# Streamlit UI
st.title("✨ Markov Chain Text Composer 📝")

# User input options
text_input = st.text_area("✍️ Enter text or upload a file:")
file = st.file_uploader("📂 Upload a text file", type=["txt"])

if file is not None:
    text_input = file.read().decode("utf-8")

order = st.slider("⚙️ Select Markov Chain Order", 1, 5, 2)
n_words = st.slider("🔢 Number of words to generate", 10, 200, 50)

generate = st.button("🚀 Generate Text")

if generate and text_input:
    markov_dict = build_markov_chain(text_input, order)
    generated_text = generate_text(markov_dict, n_words, order)
    st.subheader("🎉 Generated Text:")
    st.write(generated_text)


#random 🎲 – Yeh dice ki tarah kaam karega, random words chunega.

#re 🔍 – Yeh ek chhoti si jadoo ki chhadi hai jo text ke andar se words nikalne mein madad karegi.

#defaultdict 📦 – Yeh ek magic box hai jo words ko yaad rakhne mein madad karega.🔹 Step 1: Input Text


   #example Maan lo humare paas yeh input text hai:


#I love spicy food. I love pizza. Spicy food is tasty.
#🔹 Step 2: Markov Chain Dictionary Banayenge
#Agar order = 2 hai, toh words ko 2-word pairs ke basis pe store karenge:

#Key (2 words)	Possible Next Word
#('I', 'love')	spicy, pizza
#('love', 'spicy')	food
#('spicy', 'food')	is
#('food', 'is')	tasty
#('I', 'love')	pizza
#('love', 'pizza')	(end)
#('food', 'is')	tasty
#Ab har word pair (key) ka ek next word (value) hai.

#🔹 Step 3: Text Generation
#Maan lo, random start key ("I", "love") select hoti hai.

#"I love" → Possible next words: ["spicy", "pizza"]

#Randomly "spicy" choose hota hai.

#Sentence: I love spicy

#"love spicy" → Next word: "food"

#Sentence: I love spicy food

#"spicy food" → Next word: "is"

#Sentence: I love spicy food is

#"food is" → Next word: "tasty"

#Sentence: I love spicy food is tasty

#Final Output:
#✅ "I love spicy food is tasty"


#Maan lo randomly hum ("Mango", "is") se start karein:

#"Mango is" → Possible next words: [sweet, yellow, tasty]

#Randomly "tasty" choose hota hai.

#Sentence: Mango is tasty ✅

#"is tasty" → Next word: 🛑 (End)

#Final Output: "Mango is tasty"

#Agar dubara run karein, toh naya output ho sakta hai:

#"Mango is sweet"

#"Mango is yellow"

#💡 Toh har baar naye sentences ban sakte hain, based on previous words! 😃


#📌 Final Suggestion:
# Order = 2 ya 3 Best hai ✅
# Order = 4-5 agar zyada meaningful output chahiye 🔥
# Order = 1 mat rakho, kyunki output ajeeb lagega 😅

#Tumhare code mein already order ka slider hai (1-5), toh tum different values try kar sakte ho aur dekh sakte ho kya best kaam karta hai! 🚀😃