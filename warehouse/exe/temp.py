import random  

def main():  
    choice = random.randint(0, 9)  # 生成0到9的随机数  
    if choice <= 8:  # 如果小于或等于8，打印'右'，否则打印'左'  
        print('右')  
        second_chance()  
    else:  
        print('左')  
  
def second_chance():  
    inp = input('你现在有一个逆天改命的机会，你要不要？(y/n):').lower()  
    if inp == 'n':  
        print('OK')  
        return  
  
    correct_answers = 0  
    for _ in range(10):  
        n1 = random.randint(1, 10)  
        n2 = random.randint(1, 10)  
        inp_prompt = '{}+{}='.format(n1, n2)  
        user_input = input(inp_prompt)  
        try:  
            if int(user_input) == n1 + n2:  
                correct_answers += 1  
            else:  
                print('认真点！！')  
        except ValueError:  
            print('请输入有效的数字！')  
  
    if correct_answers < 10:  
        print('你答错了{}次，你被判为失败者'.format(10 - correct_answers))  
    else:  
        print('你答对了10次，你被判为胜利者')  
  
input('按回车键退出')  
  
if __name__ == '__main__':  
    main()