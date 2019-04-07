import smtplib #Used for the email server

#Global variables
fromemail = 'gwcgif@gmail.com' #Our email for this project
frompass = 'w3cAnd0IT!' #Our super secret password
toemail = 0 #Email that the message is sent to
message = 0 #The message (will eventually be the gif)

#Functions
def messageSending(): #Sends a message through the gmail server
    global fromemail, frompass, toemail, message
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(fromemail, frompass)
    server.sendmail(fromemail, toemail, message)
    server.quit()
    
#def takepictures():
    #Turn on the camera
    #Take a burst of picture for the gif
    #Save pictures
    #https://picamera.readthedocs.io/en/release-1.13/recipes1.html

#def makegif():
    #Compile pictures into a gif
    #Save the gif
    
#def attach():
    #global message #Store the gif here to send it in our email
    #Upload the gif
    #Attach to the email
    
def start(): #EDIT THIS ONCE ALL FUNCTIONS ARE COMPLETED!
    global fromemail, frompass, toemail, message
    toemail = input("To email address:  ")
    message = input("Message:   ")
    messageSending()
    
#Start the whole thing
start()
