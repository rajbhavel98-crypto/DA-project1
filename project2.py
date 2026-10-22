data = { "Name": [
        "Rahul",
        " Priya ",
        "AMAN",
        "rahul",
        None,
        "Riya",
        "Karan ",
        "  Neha",
        "Amit",
        "Sonal",
        "Ankit",
        "riya",
        "Vikas",
        "Pooja",
        "Rahul",
    ],
    "Age": [23, None, 150, 23, 19, 25, -5, 28, None, 45, 22, 25, 200, 30, 23],
    "City": [
        "Indore",
        " indore",
        "Delhi",
        "",
        "Mumbai",
        "Pune",
        None,
        "BHOPAL",
        "bhopal",
        "Delhi",
        "Jaipur",
        "Pune",
        "INDORE",
        "Mumbai",
        "Indore",
    ],
    "Salary": [
        "25000",
        "30,000",
        "₹45000",
        None,
        "50000",
        "40,000",
        "35000",
        "₹55,000",
        "42000",
        "",
        "28000",
        "40,000",
        "70000",
        "65000",
        "25000",
    ],
    "Email": [
        "rahul@gmail.com",
        "priya@gmail.com",
        "aman@gmail",
        None,
        "riya@gmail.com",
        "karan@yahoo.com",
        "neha@gmail.com",
        "amitgmail.com",
        "sonal@gmail.com",
        "",
        "ankit@gmail.com",
        "riya@gmail.com",
        "vikas@yahoo.com",
        "pooja@gmail.com",
        "rahul@gmail.com",
    ],
}

# ==========================================
# Clean Age
# ==========================================
for i in range(len(data["Age"])):
    if data["Age"][i] is None:
        continue
    elif data["Age"][i] < 18:
        data["Age"][i] = 18
    elif data["Age"][i] > 65:
        data["Age"][i] = 65


# ==========================================
# Clean Salary
# ==========================================
for i in range(len(data["Salary"])):
    if data["Salary"][i] is None:
        continue

    if data["Salary"][i] == "":
        data["Salary"][i] = None
        continue

    if "₹" in data["Salary"][i]:
        data["Salary"][i] = data["Salary"][i].replace("₹", "")

    if "," in data["Salary"][i]:
        data["Salary"][i] = data["Salary"][i].replace(",", "")

    if data["Salary"][i].isdigit():
        data["Salary"][i] = int(data["Salary"][i])


# ==========================================
# Clean City
# ==========================================
for i in range(len(data["City"])):
    if data["City"][i] is None:
        continue
    elif data["City"][i] == "":
        data["City"][i] = None
    else:
        data["City"][i] = data["City"][i].strip().lower().capitalize()


# ==========================================
# Clean Email (Trim & Lowercase)
# ==========================================
for i in range(len(data["Email"])):
    if data["Email"][i] is None:
        continue
    elif data["Email"][i] == "":
        data["Email"][i] = None
    else:
        data["Email"][i] = data["Email"][i].strip().lower()


# ==========================================
# Fix Email Domains
# ==========================================
for i in range(len(data["Email"])):
    if data["Email"][i] is None:
        continue
    elif data["Email"][i] == "":
        data["Email"][i] = None
    elif data["Email"][i].endswith("@yahoo.com"):
        continue
    elif data["Email"][i].endswith("@gmail"):
        data["Email"][i] += ".com"
    elif not data["Email"][i].endswith("@gmail.com"):
        data["Email"][i] += "@gmail.com"
    else:
        data["Email"][i] = data["Email"][i].strip().lower()


# ==========================================
# Remove Invalid Emails
# ==========================================
for i in range(len(data["Email"])):
    if data["Email"][i] is None:
        continue
    if len(data["Email"][i]) >= 20:
        data["Email"][i] = None


# ==========================================
# Create DataFrame
# ==========================================
df = pd.DataFrame(data)

# ==========================================
# Basic Cleaning
# ==========================================
df["Name"] = df["Name"].str.strip()
df["City"] = df["City"].str.strip()
df["Name"] = df["Name"].str.capitalize()

# ==========================================
# Fill Missing Values
# ==========================================
df["Name"] = df["Name"].fillna("Unknown")
df["City"] = df["City"].fillna("Unknown")

# ==========================================
# Remove Duplicates
# ==========================================
df.drop_duplicates(inplace=True)

# ==========================================
# Reset Index
# ==========================================
df.reset_index(drop=True, inplace=True)


for i in range(len(df)):
    if df.loc[i, "Name"] == "Unknown":
        # Copy email to Name
        df.loc[i, "Name"] = str(df.loc[i, "Email"]) if df.loc[i, "Email"] else ""

        # Check if @gmail.com is in the email
        if "@gmail.com" in df.loc[i, "Name"]:
            # Reverse the first 4 characters
            df.loc[i, "Name"] = df.loc[i, "Email"][-11::-1]

            # Reverse the newly updated string entirely
            df.loc[i, "Name"] = df.loc[i, "Name"][::-1]
            df.loc[i, "Name"] = str(df.loc[i, "Name"]).capitalize()

        elif "@yahoo.com" in df.loc[i, "Name"]:
            # Reverse the first 4 characters
            df.loc[i, "Name"] = df.loc[i, "Email"][-11::-1]

            # Reverse the newly updated string entirely
            df.loc[i, "Name"] = df.loc[i, "Name"][::-1]
            df.loc[i, "Name"] = str(df.loc[i, "Name"]).capitalize()

# ===================================================

m = int(np.mean(df["Age"].dropna()))

for i in range(len(df)):
    if pd.isna(df.loc[i, "Age"]):
        df.loc[i, "Age"] = m

# Convert the whole column to integer type after replacing NaNs
df["Age"] = df["Age"].astype(int)

# ===================================================

s = int(np.mean(df["Salary"].dropna()))

for i in range(len(df)):
    if pd.isna(df.loc[i, "Salary"]):
        df.loc[i, "Salary"] = s


for i in range(len(df["Email"])):
    if pd.isna(df.loc[i, "Email"]):
        df.loc[i, "Email"] = str(df.loc[i, "Name"]).lower() + "@gmail.com"


for i in range(len(df["Email"])):
    if df.loc[i, "Email"] and df.loc[i, "Email"][-11::-1] == df.loc[i, "Name"]:
        pass
    else:
        if df.loc[i, "Email"]:
            df.loc[i, "Name"] = df.loc[i, "Email"][-11::-1]
            df.loc[i, "Name"] = df.loc[i, "Name"][::-1].capitalize()

df