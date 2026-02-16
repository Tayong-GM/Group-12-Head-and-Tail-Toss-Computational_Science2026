import matplotlib.pyplot as plt


#insert data
new_coin_string = "1110100100101000010110011011011100100100011111010101111000000110111101010111101101100111100000100001"
old_coin_string = "0000000110110110110111001011101011011010010101100110101000011110110000101010111110011100111010100111"

#convert string to int
new_coin_flips = [int(x) for x in new_coin_string]
old_coin_flips = [int(x) for x in old_coin_string]

def calculate_cumulative(flips_list):
    """Takes a list of 1s and 0s, and returns attempts, cumulative heads, and cumulative tails."""
    heads_cum = []
    tails_cum = []
    h_count = 0
    t_count = 0

    for flip in flips_list:
        if flip == 1:
            h_count += 1
        elif flip == 0:
            t_count += 1
        
        heads_cum.append(h_count)
        tails_cum.append(t_count)

    #generate #attempts based on the length of the flips list
    attempts = list(range(1, len(flips_list) + 1))
    
    return attempts, heads_cum, tails_cum

#calculate the running totals automatically
new_attempts, new_heads, new_tails = calculate_cumulative(new_coin_flips)
old_attempts, old_heads, old_tails = calculate_cumulative(old_coin_flips)


#old coin graph
plt.figure("Old Coin (5A)", figsize=(10, 6)) 

plt.plot(old_attempts, old_heads, label='Heads Data', color='#1f77b4', linewidth=2)
plt.plot(old_attempts, old_tails, label='Tails Data', color='#ff7f0e', linestyle='--', linewidth=2)

plt.title('Old 5 Peso Coin (5A) - Cumulative Running Total', fontsize=14, fontweight='bold')
plt.xlabel('Toss Number', fontsize=12)
plt.ylabel('Running Total of H & T', fontsize=12)
plt.legend()
plt.grid(True, linestyle=':', alpha=0.6)


#new coin graph
plt.figure("New Coin (5B)", figsize=(10, 6)) 

plt.plot(new_attempts, new_heads, label='Heads Data', color='#1f77b4', linewidth=2)
plt.plot(new_attempts, new_tails, label='Tails Data', color='#ff7f0e', linestyle='--', linewidth=2)

plt.title('New 5 Peso Coin (5B) - Cumulative Running Total', fontsize=14, fontweight='bold')
plt.xlabel('Toss Number', fontsize=12)
plt.ylabel('Running Total of H & T', fontsize=12)
plt.legend()
plt.grid(True, linestyle=':', alpha=0.6)


#combined comparison
plt.figure("Combined Comparison", figsize=(12, 8)) 

#plotting new coin (blue)
plt.plot(new_attempts, new_heads, label='5B Heads (New)', color='#1f77b4', linewidth=2)
plt.plot(new_attempts, new_tails, label='5B Tails (New)', color='#87ceeb', linestyle='--', linewidth=2)

#plotting old coin (red)
plt.plot(old_attempts, old_heads, label='5A Heads (Old)', color='#d62728', linewidth=2)
plt.plot(old_attempts, old_tails, label='5A Tails (Old)', color='#ff9896', linestyle='--', linewidth=2)

plt.title('Cumulative Heads vs Tails Comparison (5B vs 5A)', fontsize=14, fontweight='bold')
plt.xlabel('Toss Number', fontsize=12)
plt.ylabel('Cumulative Count', fontsize=12)
plt.legend()
plt.grid(True, linestyle=':', alpha=0.6)

#display all graphs
print("Displaying all 3 graphs simultaneously...")
plt.show()