from mysqloperation import MySQLcaozuo

table_poll_question = "polls_question"
datas_poll_question =[ {'id': 1, 'question_text': '你喜欢的游戏是什么?'}]
table_poll_choice = "polls_choice"
datas_poll_choice =[{'id': 1, 'choice_text': '生化危机', 'votes': 0, 'question_id': 1},
                    {'id': 2, 'choice_text': 'GTA5', 'votes': 0, 'question_id': 1},]


#包括clear和insert
def insert_data(table, datas):
    db = MySQLcaozuo()
    db.clear(table)
    for data in datas:
        db.insert(table, data)
    db.close()

#update
def update_data(table,datas,condition):
    db = MySQLcaozuo()
    for data in datas:
        db.update(table,data,condition)
    db.close()

def select_data(table,conditions):
    db = MySQLcaozuo()
    for condition in conditions:
        db.select(table,condition)
    db.close()



def init_data():
    # insert 数据
    insert_data(table_poll_question, datas_poll_question)
    insert_data(table_poll_choice, datas_poll_choice)

    # update数据
    aa = "polls_question"
    bb =[ {'id': 1, 'question_text': '你喜欢的游戏是什么kkk?'}]
    update_data(aa, bb, "where id=1")

    #select数据
    cc = "polls_question"
    dd =[ {'id': 1}]
    select_data(cc, dd)

if __name__ == '__main__':
    init_data()