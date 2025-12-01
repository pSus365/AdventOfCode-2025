input_file_path = "input.txt"

try:
    with open(input_file_path, 'r') as f:
        # Wczytanie rotacji, ignorując puste linie
        rotations = [line.strip() for line in f.readlines() if line.strip()]
except FileNotFoundError:
    print(f"Błąd: Nie znaleziono pliku {input_file_path}. Upewnij się, że plik jest w tym samym katalogu.")


current_pos = 50 
zero_count = 0    

for rotation in rotations:
    direction = rotation[0]
    try:
        distance = int(rotation[1:])
    except ValueError:
        continue

    if distance == 0:
        continue

    if direction == 'R':
        k_0 = 100 - current_pos
        if k_0 == 100:
            k_0 = 100
        
        if distance >= k_0:
            zero_count += 1 + (distance - k_0) // 100
        
        current_pos = (current_pos + distance) % 100

    elif direction == 'L':
        k_0 = current_pos
        if k_0 == 0:
            k_0 = 100
        
        if distance >= k_0:
            zero_count += 1 + (distance - k_0) // 100
        
        current_pos = (current_pos - distance) % 100
        if current_pos < 0:
            current_pos += 100

print(f"Hasło (liczba razy, gdy tarcza wskazała na 0): {zero_count}")