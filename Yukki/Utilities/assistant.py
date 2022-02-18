from Yukki import (ASS_CLI_1, ASS_CLI_2, ASS_CLI_3, ASS_CLI_4, ASS_CLI_5,
                   ASSID1, ASSID2, ASSID3, ASSID4, ASSID5, ASSNAME1, ASSNAME2,
                   ASSNAME3, ASSNAME4, ASSNAME5, ASSUSERNAME1, ASSUSERNAME2,
                   ASSUSERNAME3, ASSUSERNAME4, ASSUSERNAME5)


async def get_assistant_details(assistant: int):
    if int(assistant) == 1:
        x = ASSID1
        y = ASSNAME1
        z = ASSUSERNAME1
        a = ASS_CLI_1
    elif int(assistant) == 2:
        x = ASSID2
        y = ASSNAME2
        z = ASSUSERNAME2
        a = ASS_CLI_2
    elif int(assistant) == 3:
        x = ASSID3
        y = ASSNAME3
        z = ASSUSERNAME3
        a = ASS_CLI_3
    elif int(assistant) == 4:
        x = ASSID4
        y = ASSNAME4
        z = ASSUSERNAME4
        a = ASS_CLI_4
    elif int(assistant) == 5:
        x = ASSID5
        y = ASSNAME5
        z = ASSUSERNAME5
        a = ASS_CLI_5
    return x, y, z, a
