#!/usr/bin/env python3
import string

alphabet = string.ascii_uppercase + string.digits

dec_message = []
enc_message = [202, 137, 390, 235, 114, 369, 198, 110, 350, 396, 390, 383, 225, 258, 38, 291, 75, 324, 401, 142, 288, 397]



# for val in enc_message:
#     if val % 37 < 25:
#         dec_message.append(alphabet[val % 37])
#     if val % 37 < 35:
#         dec_message.append(nums[val % 37])
#     else:
#         dec_message.append('_')

# print(dec_message)