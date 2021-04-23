from powerline_shell.themes.default import DefaultColor


class Color(DefaultColor):
    """Basic theme which only uses colors in 0-15 range"""
    USERNAME_FG = 15
    USERNAME_BG = 5
    USERNAME_ROOT_BG = 1

    HOSTNAME_FG = 5
    HOSTNAME_BG = 15

    HOME_SPECIAL_DISPLAY = True
    PATH_BG = 15  # White
    PATH_FG = 5  # Purple
    CWD_FG = 5  # Purple
    SEPARATOR_FG = 5

    READONLY_BG = 1
    READONLY_FG = 15

    REPO_CLEAN_BG = 2  # Green
    REPO_CLEAN_FG = 0  # Black
    REPO_DIRTY_BG = 1  # Red
    REPO_DIRTY_FG = 15  # White

    JOBS_FG = 14
    JOBS_BG = 8

    CMD_PASSED_BG = 8
    CMD_PASSED_FG = 15
    CMD_FAILED_BG = 11
    CMD_FAILED_FG = 0

    SVN_CHANGES_BG = REPO_DIRTY_BG
    SVN_CHANGES_FG = REPO_DIRTY_FG

    VIRTUAL_ENV_BG = 2
    VIRTUAL_ENV_FG = 0

    AWS_PROFILE_FG = 14
    AWS_PROFILE_BG = 8

    TIME_FG = 8
    TIME_BG = 7
