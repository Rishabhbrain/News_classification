

import json
import os

# Define the dictionary
my_dict = {"name": "John", "age": 30, "city": "New York",    "What is your name?": "My name is Chatbot.",
        "How are you?": "I'm doing well, thank you for asking!",
        "What do you do?": "I'm a chatbot programmed to answer your questions.",
        "What's your favorite color?": "I don't have a favorite color, I'm just a computer program.",
        "What's the meaning of life?": "That's a philosophical question that I'm not programmed to answer.",
        "What's the weather like today?": "I'm sorry, I don't know. I'm just a chatbot!",
        "What time is it?": "I don't have access to the current time.",
        "Can you tell me a joke?": "Why don't scientists trust atoms? Because they make up everything.",
        "Do you like sports?": "I don't have the ability to like or dislike things, I'm just a computer program.",
        "What's your favorite food?": "I don't eat, I'm just a computer program.",
        "What's your favorite movie?": "I don't watch movies, I'm just a computer program.",
        "Can you help me with my homework?": "I can try! What subject do you need help with?",
        "What's the capital of France?": "The capital of France is Paris.",
        "How old are you?": "I don't have an age, I'm just a computer program.",
        "What's the meaning of the word 'paradox'?": "A paradox is a statement that contradicts itself or seems impossible, but is actually true.",
        "What's your favorite book?": "I don't have a favorite book, I'm just a computer program.",
        "What's your favorite song?": "I don't have a favorite song, I'm just a computer program.",
        "Can you tell me a fun fact?": "Did you know that a group of flamingos is called a flamboyance?",
        "How do I cook pasta?": "First, bring a pot of salted water to a boil. Then, add the pasta and cook until al dente. Finally, drain the pasta and toss with your favorite sauce.",
        "What's the tallest building in the world?": "The tallest building in the world is the Burj Khalifa in Dubai, United Arab Emirates.",
        "What's the largest country in the world?": "The largest country in the world by land area is Russia.",
        "Can you translate this phrase for me?": "Sure, what language is it in and what does it mean?",
        "What's your favorite animal?": "I don't have a favorite animal, I'm just a computer program.",
        "What's your favorite hobby?": "I don't have the ability to have hobbies, I'm just a computer program.",
        "What's the square root of 144?": "The square root of 144 is 12.",
        "What's the difference between a crocodile and an alligator?": "Crocodiles have a V-shaped snout and live in saltwater habitats, while alligators have a U-shaped snout and live in freshwater habitats.",
        "What's the smallest country in the world?": "The smallest country in the world by land area is Vatican City.",
        "What's the fastest land animal?": "The fastest land animal is the cheetah.",
        "What's the highest mountain in the world?": "The highest mountain in the world is Mount Everest in Nepal."
}

# Define the file path where the JSON file will be saved
desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
file_path = os.path.join("E:\ASUSPC\Desktop", "my_dict.json")

# Write the dictionary to the JSON file
with open("E:\ASUSPC\Desktop\my_dict.json", "w") as outfile:
    json.dump(my_dict, outfile)

