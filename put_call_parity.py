def check_put_call_parity(c, p, x, r, t, s):
    lhs = c + x / (1 + r) ** t
    rhs = p + s
    if lhs == rhs:
        print("Put call parity holds")
    else:
        print("Put call parity doesn't hold")


if __name__ == "__main__":
    # asset class: rates
    check_put_call_parity(c=5, p=2, x=1, r=0, t=1, s=3)
