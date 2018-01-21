if __name__ == '__main__':
    with open('challenge-data-8.txt', 'r') as f:
        data = f.read()

    ciphertxts = data.split('\n')
    ecb_blocks = []
    for cipher in ciphertxts:
        # divide into 16-byte blocks
        blocks = [cipher[i: i+16] for i in range(0, len(cipher), 16)]

        if len(blocks) > len(set(blocks)):
            # repeating blocks!
            ecb_blocks.append(cipher)

    print(ecb_blocks)
