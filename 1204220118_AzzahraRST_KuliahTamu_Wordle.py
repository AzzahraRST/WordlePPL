def check_guess(target, guess):
    correct_position = []
    wrong_position = []
    

    for i in range(len(guess)):
        if guess[i] == target[i]:
            correct_position.append(guess[i])
    
    for digit in guess:
        if digit in target and digit not in correct_position:
            wrong_position.append(digit)
    
    return correct_position, wrong_position

def wordle_game(target, max_attempts=6):
    attempts = 0
    
    while attempts < max_attempts:
        guess = input("Masukkan tebakan (string digit): ")
        
        if len(guess) != len(target):
            print(f"Tebakan harus terdiri dari {len(target)} digit.")
            continue
        
        correct_position, wrong_position = check_guess(target, guess)
        
        print(f"Posisi benar: {''.join(correct_position)}")
        print(f"Posisi salah: {''.join(wrong_position)}")
        
        if guess == target:
            print("Selamat! Anda menang!")
            break
        
        attempts += 1
    
    if attempts == max_attempts:
        print(f"Anda kalah! Kata target adalah: {target}")


wordle_game("azzacantik")