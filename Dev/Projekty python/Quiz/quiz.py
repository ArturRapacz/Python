import requests
import html
import time
class Question:
    def __init__(self, category, questionStr, correctAnswerFlag):
        self.category = category
        self.questionStr = questionStr
        self.correctAnswerFlag = correctAnswerFlag


class Quiz:
    def __init__(self, numQuestions):
        self.apiUrl = "https://opentdb.com/api.php?difficulty=easy&type=boolean&amount="
        self.numQuestions = numQuestions
        self.questionsList = []
        self.loadQuestions(numQuestions)

    def loadQuestions(self, numQuestions):
        response = requests.get(self.apiUrl + str(numQuestions))
        #print(response.json())
        data = response.json()
        results = data["results"]

        for q in results:
            category = (q["category"])
            questionType = q["difficulty"]
            questionStr = html.unescape(q["question"])
            correctAnswerFlag = q["correct_answer"].lower() in ["true", "1", "yes"]
        
            


            qObj = Question(category,questionStr, correctAnswerFlag)
            self.questionsList.append(qObj)
            

    def startQuiz(self):
        print("\nWelcome in the quiz!")
        time.sleep(3)
        numCorrectUserAnswers = 0
        n = 0
        numQuestions = len(self.questionsList)

        while n < numQuestions:
            q = self.questionsList[n]
            print("Question number " + str(n + 1) + ": " + q.questionStr)
            answer = input("Give correct answer as yes/no: ")
            answerBool = False
            if answer.lower() == "yes":answerBool = True

            if answerBool == q.correctAnswerFlag:
                print("Correct!")
                numCorrectUserAnswers += 1
            else:
                print("Not correct!")
            time.sleep(2)

            n+=1
        print("Number of correct answers:", numCorrectUserAnswers, "from", str(len(self.questionsList)), "questions.")

quiz = Quiz(10)
quiz.startQuiz()
time.sleep(5)

question = input("Do you want to start quiz again? yes/no ")

if question.lower() == "yes":
    quiz.startQuiz()
    print("I hope you had great time with our quiz!")
    time.sleep(5)
else: 
    print("I hope you had great time with our quiz!")
    time.sleep(5)