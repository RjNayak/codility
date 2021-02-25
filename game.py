def main():

    # Write code here
    test_case_no = input()
    no_villians_lst = []
    strength_of_villians_lst = []
    strength_of_players_lst = []
    for x in range(int(test_case_no)):
        no_villians_lst.append(int(input()))
        strength_of_villians_lst.append(input().split())
        strength_of_players_lst.append(input().split())

    for i in range(0, len(no_villians_lst)):
        loss_win_lst = []
        for j in range(0, no_villians_lst[i]):
            if int(strength_of_players_lst[i][j]) > int(strength_of_villians_lst[i][j]):
                loss_win_lst.append(1)
            else:
                loss_win_lst.append(0)

        if loss_win_lst.count(1) > loss_win_lst.count(0):
            print('WIN')
        else:
            print('LOSE')


main()
