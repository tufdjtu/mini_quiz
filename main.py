from Question import Question
question_prompts = [
    "Qual o melhor marcador do euro 2016 ?\n (a)CR7 \n (b)Griezman \n (c)Giroud\n (d)Bale\n\n",
    "Onde foi disputada o primeiro campeonato de futebol?\n (a)Brasil \n (b)Inglaterra \n (c)Uruguai\n (d)Espanha\n\n",
    "Qual o melhor marcador dos campeonatos do mundo?\n (a)Klose \n (b)Pele \n (c)Rivaldo\n (d)Eusébio\n\n",
    "Quem era conhecido como Aranha Negra?\n (a)Yashin \n (b)Pele \n (c)Roberto Carlos\n (d)Weah\n\n",
    "Onde Gerard Pique estava antes de ir para o Barcelona?\n (a)Liverpool \n (b)Man .United \n (c)Atletico Madrid\n (d)Juventus\n\n"
]

questions = [
    Question(question_prompts[0],"b"),
    Question(question_prompts[1],"c"),
    Question(question_prompts[2],"a"),
    Question(question_prompts[3],"a"),
    Question(question_prompts[4],"b"),
]



def run_test(questions):
    score = 0
    for question in questions :
        answer = input(question.prompt)
        if answer == question.answer:
            score = score + 1
    print("Tivestes " + str(score) + "/" + str (len(questions)) +  " corretas")

run_test(questions)
