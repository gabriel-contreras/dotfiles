from powerline_shell.themes.default import DefaultColor


class Color(DefaultColor):
    USERNAME_FG = 129
    USERNAME_BG = 233
    USERNAME_ROOT_BG = 1

    HOSTNAME_FG = 5
    HOSTNAME_BG = 235

    HOME_SPECIAL_DISPLAY = False
    PATH_BG = 233
    PATH_FG = 5
    CWD_FG = 129
    SEPARATOR_FG = 129

    READONLY_BG = 1
    READONLY_FG = 15

    REPO_CLEAN_BG = 2
    REPO_CLEAN_FG = 0
    REPO_DIRTY_BG = 1
    REPO_DIRTY_FG = 15

    JOBS_FG = 14
    JOBS_BG = 8

    CMD_PASSED_BG = 235
    CMD_PASSED_FG = 5
    CMD_FAILED_BG = 5
    CMD_FAILED_FG = 235

    SVN_CHANGES_BG = REPO_DIRTY_BG
    SVN_CHANGES_FG = REPO_DIRTY_FG

    VIRTUAL_ENV_BG = 2
    VIRTUAL_ENV_FG = 0

    AWS_PROFILE_FG = 14
    AWS_PROFILE_BG = 8

    TIME_FG = 8
    TIME_BG = 7
