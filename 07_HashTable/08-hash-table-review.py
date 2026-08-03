# ==========================================
# Hash Table Review
# ==========================================

# Hash Table
#
# Purpose:
# Store Key-Value pairs.
#
# Average Time Complexity
# Insert : O(1)
# Search : O(1)
# Remove : O(1)
#
# Worst Case
# O(n)


# ==========================================
# 1. Hash Function
# ==========================================

# Convert a key into an array index.

def hash(key):
    total = 0

    for char in key:
        total += ord(char)

    return total % 10


# ==========================================
# 2. Insert
# ==========================================

# key
#   ↓
# hash()
#   ↓
# index
#   ↓
# table[index]


# ==========================================
# 3. Collision
# ==========================================

# Two different keys produce the same index.


# ==========================================
# 4. Separate Chaining
# ==========================================

# Array
#
# 2
# │
# ▼
# cat -> dog -> apple -> None
#
# Use Linked List.


# ==========================================
# 5. Linear Probing
# ==========================================

# Collision
#
# 2 occupied
# ↓
# 3 occupied
# ↓
# 4 empty
# ↓
# Put data in index 4.


# ==========================================
# 6. Search
# ==========================================

# hash(key)
# ↓
# Compare keys
# ↓
# Found -> return value


# ==========================================
# 7. Remove
# ==========================================

# Basic
#
# table[index] = None
#
# Problem:
# Search may stop too early.


# ==========================================
# 8. Tombstone
# ==========================================

# Instead of None
#
# DELETED
#
# Search continues.


# ==========================================
# 9. Wrap Around
# ==========================================

# index = (index + 1) % len(table)
#
# 9
# ↓
# 0
# ↓
# 1


# ==========================================
# Hash Table Summary
# ==========================================

# Hash Function
#        ↓
#      Insert
#        ↓
#    Collision
#      /    \
# Chaining  Linear Probing
#                ↓
#       Search / Remove
#                ↓
#      Tombstone / Wrap Around