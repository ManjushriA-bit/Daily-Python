# 1️⃣ Check eligibility
def check_eligibility(age):
    return age >= 18


# 2️⃣ Display candidates
def show_candidates(candidates):
    print("\nCandidates:")
    for c in candidates:
        print("-", c.capitalize())


# 3️⃣ Cast a single vote
def cast_vote():
    return input("Enter candidate name: ").lower()


# 4️⃣ Count votes
def calculate_vote_count(vote_list):
    count = {}
    for vote in vote_list:
        if vote in count:
            count[vote] += 1
        else:
            count[vote] = 1
    return count


# 5️⃣ Display results using **kwargs
def display_results(**vote_count):
    print("\n--- Voting Results ---")
    for candidate, votes in vote_count.items():
        print(candidate.capitalize(), ":", votes)


# 6️⃣ Find winner using lambda
def find_winner(vote_count):
    return max(vote_count.items(), key=lambda x: x[1])


# ================= MAIN PROGRAM =================

candidates = ["alice", "bob", "charlie"]
votes = []

while True:
    age = int(input("\nEnter your age: "))

    if not check_eligibility(age):
        print("Not eligible to vote.")
    else:
        show_candidates(candidates)
        vote = cast_vote()

        if vote in candidates:
            votes.append(vote)
            print("Vote recorded successfully.")
        else:
            print("Invalid candidate.")

    choice = input("\nDo you want to continue voting? (yes/no): ").lower()
    if choice == "no":
        break


# After voting ends
if votes:
    vote_count = calculate_vote_count(votes)
    display_results(**vote_count)

    winner, total_votes = find_winner(vote_count)
    print("\nWinner:", winner.capitalize())
    print("Votes:", total_votes)
else:
    print("\nNo votes were cast.")
