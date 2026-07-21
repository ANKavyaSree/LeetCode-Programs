def maximize_active_sections(s):
    ones = s.count("1")
    best_gain = 0

    t = "1" + s + "1"

    i = 1
    while i < len(t) - 1:
        if t[i] == "1":
            start = i

            while i < len(t) and t[i] == "1":
                i += 1

            end = i

            if t[start - 1] == "0" and t[end] == "0":
                left = start - 1
                while left >= 0 and t[left] == "0":
                    left -= 1

                right = end
                while right < len(t) and t[right] == "0":
                    right += 1

                left_zero_count = start - left - 1
                right_zero_count = right - end

                best_gain = max(
                    best_gain,
                    left_zero_count + right_zero_count
                )
        else:
            i += 1

    return ones + best_gain


s = input("Enter the binary string: ")

print("Maximum active sections:", maximize_active_sections(s))
