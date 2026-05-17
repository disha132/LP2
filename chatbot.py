print("=== College Enquiry Chatbot ===")
print("Type 'bye' to exit\n")

while True:
    user = input("You: ").lower()

    if "course" in user:
        print("Bot: We offer BTech, MBA, BCA, and MCA courses.")

    elif "fees" in user:
        print("Bot: The average annual fee is Rs. 80,000.")

    elif "admission" in user:
        print("Bot: Admissions start from June every year.")

    elif "hostel" in user:
        print("Bot: Hostel facilities are available for boys and girls.")

    elif user == "bye":
        print("Bot: Thank you!")
        break

    else:
        print("Bot: Please ask college-related questions.")
