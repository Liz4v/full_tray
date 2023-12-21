import itertools
import winreg


def main():
    access1 = winreg.KEY_READ
    access2 = winreg.KEY_SET_VALUE | winreg.KEY_QUERY_VALUE
    key_path = r"Control Panel\NotifyIconSettings"
    super_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, key_path, access=access1)
    for index in itertools.count():
        try:
            name = winreg.EnumKey(super_key, index)
        except OSError:
            break  # no more keys
        subkey = winreg.OpenKey(super_key, name, access=access2)
        examine(name, subkey)
        winreg.CloseKey(subkey)
    winreg.CloseKey(super_key)
    # noinspection PyUnboundLocalVariable
    print(f"Done for {index} keys")


def examine(name, subkey):
    try:
        value, type_ = winreg.QueryValueEx(subkey, "IsPromoted")
        if value == 1 and type_ == winreg.REG_DWORD:
            return  # already correct
    except FileNotFoundError:
        pass  # new
    winreg.SetValueEx(subkey, "IsPromoted", 0, winreg.REG_DWORD, 1)
    try:
        value, _ = winreg.QueryValueEx(subkey, "ExecutablePath")
    except FileNotFoundError:
        value = "unknown path"
    print(f"Set IsPromoted=1 for {name} ({value})")


if __name__ == "__main__":
    main()
