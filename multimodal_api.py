from gradio_client import Client, handle_file

client = Client("http://localhost:8080/")
result = client.predict(
    image=handle_file('img.jpg'),
    _chatbot=[],
    api_name="/upload_img"
)

print("-----------upload--------------")
print(result)

result = client.predict(
    _question="What's in the image?",
    _chat_bot=[result[0]],  # Use the chat_bot returned from the previous step
    api_name="/request"
)
print("-----------request--------------")
print(result)

result = client.predict(
    _chat_bot=result[1],  # Use the chat_bot returned from the previous step
    params_form="Sampling",
    num_beams=3,
    repetition_penalty=1.2,
    repetition_penalty_2=1.05,
    top_p=0.8,
    top_k=100,
    temperature=0.7,
    api_name="/respond"
)
print("-----------respond--------------")
print(result)

print("-----------Final answer--------------")
print(result[-1][-1])