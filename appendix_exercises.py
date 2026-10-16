# ==========================================
# APPENDIX EXERCISE 1
# ENGINEERING TEST DATA ORGANIZER
# ==========================================

LAST_NAME = "Juarez"
STUDENT_ID = "TUPM-26-1843"
FAVORITE_ARTIST = "Arthur Nery"

# Assumption: use the last digit of the student ID as the seed.
SEED_NUM = int(STUDENT_ID[-1])

# Generate five test sources.
test_sources = [
    LAST_NAME + "_T1",
    LAST_NAME + "_T2",
    LAST_NAME + "_T3",
    LAST_NAME + "_T4",
    LAST_NAME + "_T5"
]

categories = [
    "TEMPERATURE",
    "VOLTAGE",
    "CURRENT",
    "PRESSURE",
    "SPEED"
]

# Get alphabet positions from the favorite artist's name.
artist_positions = [
    ord(letter.upper()) - ord("A") + 1
    for letter in FAVORITE_ARTIST
    if letter.isalpha()
]

# Generate measurement records.
test_records = []

for i, source in enumerate(test_sources):
    for j, category in enumerate(categories):
        position = artist_positions[
            (i + j) % len(artist_positions)
        ]

        value = SEED_NUM + position + i + j

        test_records.append({
            "source": source,
            "category": category,
            "value": value
        })

# Add a repeated source-category record.
test_records.append(test_records[0].copy())

print("=== GENERATED TEST DATA ===")
for record in test_records:
    print(record)

# Organize records by source and category.
organized_data = {}

for record in test_records:
    source = record["source"]
    category = record["category"]

    if source not in organized_data:
        organized_data[source] = {}

    if category not in organized_data[source]:
        organized_data[source][category] = []

    organized_data[source][category].append(record["value"])

print("\n=== ORGANIZED TEST DATA ===")
for source, measurements in organized_data.items():
    print(source, ":", measurements)

# Identify repeated and distinct source-category pairs.
record_pairs = [
    (record["source"], record["category"])
    for record in test_records
]

distinct_pairs = set(record_pairs)

print("\n=== REPEATED AND DISTINCT DATA ===")
print("Total Records:", len(test_records))
print("Distinct Source-Category Pairs:", len(distinct_pairs))

for pair in distinct_pairs:
    count = record_pairs.count(pair)
    if count > 1:
        print("Repeated:", pair, "Count:", count)

# Numerical summary.
values = [record["value"] for record in test_records]

print("\n=== NUMERICAL SUMMARY ===")
print("Minimum:", min(values))
print("Maximum:", max(values))
print("Total:", sum(values))
print("Average:", round(sum(values) / len(values), 2))

# Categorical summary.
print("\n=== CATEGORICAL SUMMARY ===")
for category in categories:
    count = sum(
        1 for record in test_records
        if record["category"] == category
    )
    print(category, ":", count)

# Order records by measurement value.
ordered_records = sorted(
    test_records,
    key=lambda record: record["value"]
)

print("\n=== ORDERED RESULTS ===")
for record in ordered_records:
    print(record)

print("\n=== FINAL TEST DATA SUMMARY ===")
print("Test Sources:", len(test_sources))
print("Measurement Categories:", len(categories))
print("Total Records:", len(test_records))
print("Distinct Pairs:", len(distinct_pairs))
print("Repeated Records:", len(test_records) - len(distinct_pairs))


# ==========================================
# APPENDIX EXERCISE 2
# STUDENT PERFORMANCE DATA ANALYZER
# ==========================================

# Student-specific information.
LAST_NAME = "Juarez"
STUDENT_ID = "TUPM-26-1843"
FAVORITE_ARTIST = "Arthur Nery"
SEED_NUM = int(STUDENT_ID[-1])

student_names = [
    LAST_NAME + "_S1",
    LAST_NAME + "_S2",
    LAST_NAME + "_S3",
    LAST_NAME + "_S4",
    LAST_NAME + "_S5"
]

subjects = [
    "PROGRAMMING",
    "MATHEMATICS",
    "ELECTRONICS",
    "PHYSICS",
    "ENGLISH"
]

artist_positions = [
    ord(letter.upper()) - ord("A") + 1
    for letter in FAVORITE_ARTIST
    if letter.isalpha()
]

performance_records = []

for i, student in enumerate(student_names):
    for j, subject in enumerate(subjects):
        position = artist_positions[
            (i + j) % len(artist_positions)
        ]

        score = (SEED_NUM * 10 + position + i * 5 + j) % 101

        performance_records.append({
            "student": student,
            "subject": subject,
            "score": score
        })

# Add one repeated student-subject record.
performance_records.append(performance_records[0].copy())

# Add one incomplete record.
performance_records.append({
    "student": student_names[0],
    "subject": "PHYSICS",
    "score": None
})

# Determine performance category.
def performance_category(score):
    if score is None:
        return "INCOMPLETE"
    elif score >= 90:
        return "Excellent"
    elif score >= 80:
        return "Very Good"
    elif score >= 75:
        return "Passed"
    else:
        return "Needs Improvement"

for record in performance_records:
    record["category"] = performance_category(record["score"])

print("=== GENERATED PERFORMANCE RECORDS ===")
for record in performance_records:
    print(record)

# Organize by student and subject.
organized_records = {}

for record in performance_records:
    student = record["student"]
    subject = record["subject"]

    if student not in organized_records:
        organized_records[student] = {}

    organized_records[student].setdefault(subject, []).append(
        record["score"]
    )

print("\n=== ORGANIZED STUDENT DATA ===")
for student, data in organized_records.items():
    print(student, ":", data)

# Identify repeated records.
record_keys = [
    (record["student"], record["subject"])
    for record in performance_records
]

print("\n=== REPEATED RECORDS ===")
for key in set(record_keys):
    if record_keys.count(key) > 1:
        print(key, "Count:", record_keys.count(key))

# Identify incomplete records.
print("\n=== INCOMPLETE RECORDS ===")
for record in performance_records:
    if record["score"] is None:
        print(record)

# Student summaries.
print("\n=== STUDENT PERFORMANCE SUMMARY ===")
for student in student_names:
    scores = [
        record["score"]
        for record in performance_records
        if record["student"] == student
        and record["score"] is not None
    ]

    if scores:
        print(
            student,
            "Average:", round(sum(scores) / len(scores), 2)
        )

# Subject summaries.
print("\n=== SUBJECT PERFORMANCE SUMMARY ===")
for subject in subjects:
    scores = [
        record["score"]
        for record in performance_records
        if record["subject"] == subject
        and record["score"] is not None
    ]

    if scores:
        print(
            subject,
            "Average:", round(sum(scores) / len(scores), 2)
        )

# Ordered results.
ordered_records = sorted(
    performance_records,
    key=lambda record: (
        record["score"] is None,
        record["score"] if record["score"] is not None else 0
    ),
    reverse=True
)

print("\n=== ORDERED RESULTS ===")
for record in ordered_records:
    print(record)

print("\n=== FINAL STUDENT PERFORMANCE REPORT ===")
print("Total Records:", len(performance_records))
print("Students:", len(student_names))
print("Subjects:", len(subjects))
print(
    "Incomplete Records:",
    sum(1 for r in performance_records if r["score"] is None)
)


# ==========================================
# APPENDIX EXERCISE 3
# TRANSACTION HISTORY ANALYZER
# ==========================================

LAST_NAME = "Juarez"
STUDENT_ID = "TUPM-26-1843"
FAVORITE_ARTIST = "Arthur Nery"
SEED_NUM = int(STUDENT_ID[-1])

customers = [
    LAST_NAME + "_C1",
    LAST_NAME + "_C2",
    LAST_NAME + "_C3",
    LAST_NAME + "_C4",
    LAST_NAME + "_C5"
]

# Fixed prices in pesos.
product_prices = {
    "NOTEBOOK": 50,
    "PEN": 15,
    "USB": 250,
    "HEADPHONES": 500,
    "CALCULATOR": 300
}

products = list(product_prices.keys())

artist_positions = [
    ord(letter.upper()) - ord("A") + 1
    for letter in FAVORITE_ARTIST
    if letter.isalpha()
]

transactions = []

for i, customer in enumerate(customers):
    for j, product in enumerate(products):
        position = artist_positions[
            (i + j) % len(artist_positions)
        ]

        quantity = ((SEED_NUM + position + i + j) % 5) + 1
        price = product_prices[product]

        transactions.append({
            "customer": customer,
            "product": product,
            "quantity": quantity,
            "unit_price": price,
            "transaction_value": quantity * price
        })

# Add one repeated customer-product purchase.
transactions.append(transactions[0].copy())

print("=== PRODUCT PRICES ===")
for product, price in product_prices.items():
    print(product, ": PHP", price)

print("\n=== GENERATED TRANSACTIONS ===")
for transaction in transactions:
    print(transaction)

# Identify repeated customer-product pairs.
purchase_pairs = [
    (t["customer"], t["product"])
    for t in transactions
]

distinct_pairs = set(purchase_pairs)

print("\n=== REPEATED PURCHASES ===")
for pair in distinct_pairs:
    if purchase_pairs.count(pair) > 1:
        print(pair, "Count:", purchase_pairs.count(pair))

print("\n=== DISTINCT CUSTOMERS AND PRODUCTS ===")
print("Customers:", set(t["customer"] for t in transactions))
print("Products:", set(t["product"] for t in transactions))

# Calculate overall transaction value.
print("\n=== TRANSACTION VALUES ===")
for transaction in transactions:
    print(
        transaction["customer"],
        transaction["product"],
        "Value: PHP",
        transaction["transaction_value"]
    )

overall_total = sum(
    t["transaction_value"] for t in transactions
)

# Customer summaries.
print("\n=== CUSTOMER SUMMARY ===")
for customer in customers:
    total = sum(
        t["transaction_value"]
        for t in transactions
        if t["customer"] == customer
    )
    print(customer, ": PHP", total)

# Product summaries.
print("\n=== PRODUCT SUMMARY ===")
for product in products:
    total = sum(
        t["transaction_value"]
        for t in transactions
        if t["product"] == product
    )
    print(product, ": PHP", total)

# Order transactions by transaction value.
ordered_transactions = sorted(
    transactions,
    key=lambda t: t["transaction_value"],
    reverse=True
)

print("\n=== ORDERED TRANSACTIONS ===")
for transaction in ordered_transactions:
    print(transaction)

print("\n=== FINAL CONSOLIDATED TRANSACTION REPORT ===")
print("Total Customers:", len(customers))
print("Distinct Products:", len(products))
print("Total Transaction Records:", len(transactions))
print("Distinct Customer-Product Pairs:", len(distinct_pairs))
print("Overall Transaction Value: PHP", overall_total)