class py_solution:
    def roman_to_int(self, s):
        # Bảng giá trị số La Mã
        rom_val = {
            'I': 1, 'V': 5, 'X': 10,
            'L': 50, 'C': 100, 'D': 500, 'M': 1000
        }

        int_val = 0

        # Duyệt từng ký tự
        for i in range(len(s)):
            # Nếu ký tự hiện tại lớn hơn ký tự trước đó → dạng trừ (IV, IX,…)
            if i > 0 and rom_val[s[i]] > rom_val[s[i - 1]]:
                int_val += rom_val[s[i]] - 2 * rom_val[s[i - 1]]
            else:
                int_val += rom_val[s[i]]

        return int_val


# -------------------------------
# Chạy thử theo flowchart
# -------------------------------
print(py_solution().roman_to_int('MMMCMLXXXVI')) 
print(py_solution().roman_to_int('C'))
print(py_solution().roman_to_int('MMMM'))
