from IPython.display import display, HTML, Image, clear_output
import time
import random

import requests
from bs4 import BeautifulSoup
import json
import time

print("We are going to test your memory!")

print("Please enter your name:")
Name = input("> ")

print("Please enter your age:")
Age = input("> ")

print("Please enter your gender:")
Gender = input("> ")

print("Please enter the year you are currently in:")
Year = input("> ")

print("Please enter the course you are currently pursuing:")
Course = input("> ")

# Assuming array1.JPG, array2.JPG, array3.JPG are images stored in your Jupyter notebook directory
array1 = Image("Array1.JPG", width = 1000)
array2 = Image("Array2.JPG", width = 1000)
array3 = Image("Array3.JPG", width = 1000)
array4 = Image("Array4.JPG", width = 1000)
array5 = Image("Array5.JPG", width = 1000)
array6 = Image("Array6.JPG", width = 1000)

def run_memory():
    def rules():
        colors = ['blue', 'green', 'red', 'purple', 'orange']
        circle_image = 'O.jpg'  
        
        text = "THE MEMORY TEST"
        colored_text = ""
        
        for char in text:
            if char == 'O':
                colored_text += f"<img src='{circle_image}' style='width: 24px; height: 24px;'/>"
            else:
                colored_text += f"<span style='color: {random.choice(colors)}'>{char}</span>"
        
        text1 = HTML(f"<h1>{colored_text}</h1>")
        display(text1)
        time.sleep(2)
        
        text2 = HTML("<h3>Hi! Before taking the memory test, we would first like to set some rules and introduce you to what you may expect!</h3>")
        text3 = HTML("<h3>This test consists of 6 rounds. In each round, an image with different shapes of different colors will be shown!</h3>")
        text4 = HTML("<h3>However, each image will be shown only for a limited period of time. Your goal is to memorise as much from the image as possible!</h3>")
        text5 = HTML("<h3>You will be asked questions about the shapes, including their position within the grid, their color or the shape they share the box with!</h3>")
        text6 = HTML("<h3>You will be marked based on the correctness of your answers. There is not a time limit for the answers!</h3>")
        text7 = HTML("<h3>You will be marked based on the correctness of your answers. There is not a time limit for the answers!</h3>")
        text8 = HTML("<h3>You will be marked based on the correctness of your answers. There is not a time limit for the answer!</h3>")
        text9 = HTML("<h3>To ensure that you're really teasing your brain, we would like to ask you not to take pictures of the displayed images, nor to consult your answers with your peers.</h3>")
        text10 = HTML("<h3>That is all! We wish you a good luck!</h3>")
        
        temp_display = display(text2, display_id=True)
        time.sleep(5)
        clear_output(wait=True)
        
        temp_display = display(text3, display_id=True)
        time.sleep(5)
        clear_output(wait=True)
        
        temp_display = display(text4, display_id=True)
        time.sleep(8)
        clear_output(wait=True)
        
        temp_display = display(text5, display_id=True)
        time.sleep(8)
        clear_output(wait=True)
        
        temp_display = display(text6, display_id=True)
        time.sleep(3)
        clear_output(wait=True)
        
        temp_display = display(text7, display_id=True)
        time.sleep(5)
        clear_output(wait=True)
        
        temp_display = display(text8, display_id=True)
        time.sleep(5)
        clear_output(wait=True)
        
        temp_display = display(text9, display_id=True)
        time.sleep(8)
        clear_output(wait=True)
        
        temp_display = display(text10, display_id=True)
        time.sleep(5)
        clear_output(wait=True)
                
        clear_output()
        
    rules()
    
    count = 0
    arraypics = [array1, array2, array3, array4, array5, array6]
    
    
    qs1 = {"What is the color of the triangle?" : "blue",
           "In which box is the square located?" : "1",
           "What is the color of the circle?" : "green"}

    qs2 = {"What is the color of the square?" : "yellow",
           "In which box is the circle located?" : "3",
           "In which box is the triangle located?" : "green"}

    qs3 = {"Which one is bigger: the arrow or the square?" : "square",
           "In which box is the star located?" : "2",
           "What shape is in the same box as the triangle?" : "square"}

    qs4 = {"Which one is bigger: the star or the plus sign?" : "star",
           "In which box is the arrow located?" : "1",
           "What shape is in the same box as the circle?" : "plus sign"}

    qs5 = {"What color is the square?" : "green",
           "In which box is the circle?" : "2",
           "What shape is in the same box as the star?" : "arrow"}

    qs6 = {"Which one is bigger: the circle or the plus sign?" : "circle",
           "What shape is in the same box as the triangle?" : "square",
           "What shape is in the same box as the arrow?" : "square"}
    
    
    
    count = 0
    arraypics = [array1, array2, array3, array4, array5, array6]
    arrayqs = {array1 : qs1, array2: qs2, array3: qs3, array4: qs4, array5: qs5, array6: qs6}
    
    
    
    questions = []
    answers = []
    
    for i, displayedarray in enumerate(arraypics):
        display(displayedarray)
        time.sleep(1 if i < 7 else 15)
        clear_output()
    
        for q in arrayqs[displayedarray]:
            questions.append(q)
            print(q)
            answer = input().lower()
            answers.append(answer)
            clear_output()
    
    # Store each question and its answer as a separate variable
    q_and_a_list = []
    for i, answer in enumerate(answers, start=1):
        q_and_a_list.append((f"q{i}ans", answer))

    return q_and_a_list

   
    # Display the final message
    if count <=9: 
        message = f"<h3>Thank you for doing the test! You've scored {count} points out of 18. Don't worry, you'll get it next time!</h3>"
    else:
        message = f"<h3>Thank you for doing the test! You've scored {count} points out of 18. Well done!</h3>"
    display(HTML(message))


q_and_a_list = run_memory()

# Data dictionary setup
data_dict = {"Name": Name, "Age": Age, "Gender": Gender, "Year": Year, "Course": Course}
data_dict.update(dict(q_and_a_list))

form_url = "https://docs.google.com/forms/d/e/1FAIpQLScqSgfGr31lvvgKkCHgXmcMd8jDg0QrzU0ocnTetF-Y_Zei5g/viewform?usp=sf_link"

# Google Forms submission function
def send_to_google_form(data_dict, form_url):
    ''' Helper function to upload information to a corresponding google form 
        You are not expected to follow the code within this function!
    '''
    form_id = form_url[34:90]
    view_form_url = 'https://docs.google.com/forms/d/e/1FAIpQLScqSgfGr31lvvgKkCHgXmcMd8jDg0QrzU0ocnTetF-Y_Zei5g/viewform?usp=sf_link'
    post_form_url = 'https://docs.google.com/forms/d/e/1FAIpQLScqSgfGr31lvvgKkCHgXmcMd8jDg0QrzU0ocnTetF-Y_Zei5g/formResponse'

    page = requests.get(view_form_url)
    content = BeautifulSoup(page.content, "html.parser").find('script', type='text/javascript')
    content = content.text[27:-1]
    result = json.loads(content)[1][1]
    form_dict = {}
    
    loaded_all = True
    for item in result:
        if item[1] not in data_dict:
            print(f"Form item {item[1]} not found. Data not uploaded.")
            loaded_all = False
            return False
        form_dict[f'entry.{item[4][0][0]}'] = data_dict[item[1]]
    
    post_result = requests.post(post_form_url, data=form_dict)
    print(post_result.status_code, post_result.text)
    return post_result.ok

send_to_google_form(data_dict, form_url)



