class UserSystem:
    user = {}

    def __init__(self):
        with open("UserList.txt", "r") as f:
            lines = f.readlines()  # "유저 키워드1 키워드2 ..." 형태로 되어있는 모든 줄을 읽음
            for line in lines:
                user_keywords = line.split()  # "유저", "키워드1", "키워드2", ... 형식으로 스플릿
                UserSystem.user[user_keywords[0]] = []  # 딕셔너리에 저장하는 로직
                for keyword in user_keywords[1:]:
                    UserSystem.user[user_keywords[0]].append(keyword)

    def add_keyword(self, email, keyword):
        if (not email in UserSystem.user):
            UserSystem.user[email] = []
        # 키워드에 대해 중복이 없다면
        if keyword in UserSystem.user[email]:
            return "실패 - 입력한 키워드가 이미 등록한 키워드인지 확인해주세요."
        else:
            UserSystem.user[email].append(keyword)
            return "성공"

    def remove_keyword(self, email, keyword):
        if email in UserSystem.user:
            # 등록한 키워드라면,
            if keyword in UserSystem.user[email]:
                UserSystem.user[email].remove(keyword)
                return "성공"
            # 등록하지 않은 키워드라면,
            else:
                return "실패 - 등록되지 않은 키워드입니다. 오타가 있는지 확인하세요."
        else:
            return "실패 - 등록되지 않은 이메일입니다. 먼저 키워드 등록을 먼저 진행하세요."

    def check_keyword(self, email):
        if email in UserSystem.user:
            return UserSystem.user[email]
        else:
            return "등록되지 않은 유저입니다."

    def file_program_synch(self):
        with open("UserList.txt", "w") as f:
            for key, value in UserSystem.user.items():
                f.write(key+" ")
                for word in value:
                    f.write(word+" ")
                f.write('\n')
