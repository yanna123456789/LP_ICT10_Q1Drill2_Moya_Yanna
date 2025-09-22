from pyscript import document

def generate_message(event):

    name = document.getElementById("name").value
    age = document.getElementById("age").value
    school = document.getElementById("school").value


    message = f"""
    <h3>Student Info</h3>
    <p><b>Name:</b> {name}</p>
    <p><b>Age:</b> {age}</p>
    <p><b>School:</b> {school}</p>
    <hr>
    <p>✏️Notes:</p>
    {name} is currently {age} years old and studies at {school} </br>
    This information was gathered through input fields and displayed 
    using a multiline string in Python via pyscript</p>
    """

    message_if_black = "Please Fill in all fields."

    # Output to the page
    output = document.getElementById("output")
    if name == "" or age == "" or school == "":
        output.innerHTML = message_if_black
    else:
        output.innerHTML = message
