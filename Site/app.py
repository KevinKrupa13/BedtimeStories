import os
from story import write_story, append_to_story, session_prompt

def ghostWritter(userStory):
    #userStory = input("Enter your prompt: ")
    print("\n\n#####################################\n#####################################\n#####################################")
    print("------And so your tale begins--------\n\n")
    #session_story = "The following is a spooky story written for kids, just in time for Halloween. Everyone always talks about the old house at the end of the street, but I couldn't believe what happened when I went inside."
    session_story = "The following is a story written for kid about " + userStory 
    story = ""
    for i in range(0, 1):
        story = write_story(session_story)
        session_story = append_to_story(story, session_story)
    print(session_story)
    return session_story
    print("\n\n--------------The end----------------")
    print("#####################################\n#####################################\n#####################################\n\n")



#if __name__ == "__main__":
 #   ghostWritter()