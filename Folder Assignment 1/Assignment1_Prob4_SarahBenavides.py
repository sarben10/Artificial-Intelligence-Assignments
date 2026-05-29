# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 20:16:39 2025

@author: sarah
"""

class Chatbot:
    
    def __init__(self, name):
        
        self.name = name  #initialize name
        
        #private dictionary for predefined input/output pairs
        self.__responses = {
        
            "hello": "Hello! How can I assist you?",
            "bye": "Goodbye! Have a great day!",
            "help": "Available inputs: hello, bye, help" 
        }
        
    def respond(self, user_input):
        
        self.user_input = user_input
        
        i = {1: "hello", 2: "bye", 3: "help"}
        
        
        if user_input in self.__responses:   #looking up inputs
            
            return self.__responses[user_input]  #takes string as input and returns appropriate output
        
        else:
            return "I do not understand that input"  #if input isn't found
        
        
    def get_name(self):   #return chatbot name
        
        return self.name
    
    def get_available_inputs(self):   #return list of inputs from __responses
        
        return list(self.__responses.keys())
    
    
    
if __name__ == "__main__":
    
    robot = Chatbot("PythonBot3000")
    
    testing_user_inputs = ["hello", "bye", "help", "dog"]
    
    for user_str in testing_user_inputs:
        print("User: ", user_str)  
        print("Robot: ", robot.respond(user_str))  
    
    print("Chatbot's name: ", robot.get_name())
    print("Available inputs: ", robot.get_available_inputs())
        