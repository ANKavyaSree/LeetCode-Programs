# Day 181 - Count Days Spent Together
# User input program

def count_days_together(arrive_alice, leave_alice, arrive_bob, leave_bob):
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    def to_day(date):
        month, day = map(int, date.split("-"))
        return sum(days_in_month[:month - 1]) + day

    start = max(to_day(arrive_alice), to_day(arrive_bob))
    end = min(to_day(leave_alice), to_day(leave_bob))

    return max(0, end - start + 1)


arrive_alice = input("Enter Alice's arrival date (MM-DD): ").strip()
leave_alice = input("Enter Alice's leaving date (MM-DD): ").strip()
arrive_bob = input("Enter Bob's arrival date (MM-DD): ").strip()
leave_bob = input("Enter Bob's leaving date (MM-DD): ").strip()

result = count_days_together(arrive_alice, leave_alice, arrive_bob, leave_bob)
print("Days spent together:", result)
