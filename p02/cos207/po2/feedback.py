VALID = {"CSC", "SEN", "CYB", "IFT", "DTS"}
def valid_matric(m):
 parts = m.split("/")
 return (len(parts) == 3 and parts[0] == "WSU" and parts[1].isdigit()
 and len(parts[2]) == 4 and parts[2].isdigit())







words_total = 0
with open("data/feedback.txt", encoding="utf-8") as f:
    for line in f:
        matric, prog, comment = [p.strip() for p in line.split(";")]
        matric, prog = matric.upper(), prog.upper()
        if not valid_matric(matric) or prog not in VALID:
            print("REJECT", matric, prog)
            continue
        n = len(comment.split())
        words_total += n
        label = "short" if n < 4 else "long" if n > 10 else "medium"
        print(f"{matric} {prog} {n:>2} words ({label})")

print("Total words:", words_total)