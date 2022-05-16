import sys
from UserSystem import UserSystem


if __name__ == "__main__":
    user_system = UserSystem()

    while True:
        menu_num = int(
            input("1. 키워드 등록\n2. 키워드 조회\n3. 키워드 삭제\n4. 종료\n1, 2, 3, 4 중 하나를 입력해주세요 : "))
        if(menu_num == 1):
            email, keyword = input("이메일과 키워드를 띄어쓰기하여 입력해주세요(ex : honggildong@gmail.com 맥북) : ").split()
            print(user_system.add_keyword(email, keyword))
        elif(menu_num == 2):
            email = input("이메일을 입력해주세요(ex : honggildong@gmail.com) : ")
            print(user_system.check_keyword(email))
        elif(menu_num == 3):
            email, keyword = input("이메일과 키워드를 띄어쓰기하여 입력해주세요(ex : honggildong@gmail.com 맥북) : ").split()
            print(user_system.remove_keyword(email, keyword))
        elif(menu_num == 4):
            user_system.file_program_synch()
            sys.exit(0)
        else:
            print("다른 입력을 원합니다.")
