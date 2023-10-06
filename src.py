import math

def calculate_angle(A, B, C):
    # Calculates the angle ABC using dot product
    BA = [A[0]-B[0], A[1]-B[1]]
    BC = [C[0]-B[0], C[1]-B[1]]
    
    dot_product = BA[0]*BC[0] + BA[1]*BC[1]
    cross_product = BA[0]*BC[1] - BA[1]*BC[0]
    
    angle = math.atan2(cross_product, dot_product)
    return math.degrees(angle)

def classify_skeletal_relationship(ANB):
    if 2 <= ANB <= 4:
        return "Normal Skeletal Relationship"
    elif ANB > 4:
        return "Class II Skeletal Relationship"
    else:
        return "Class III Skeletal Relationship"

def maxillary_position(SNA):
    if SNA < 84:
        return "Maxillary Retrognathism"
    else:
        return "Maxillary Prognathism"

def mandibular_position(SNB):
    if SNB < 78:
        return "Mandibular Retrognathism"
    elif SNB > 82:
        return "Mandibular Prognathism"
    else:
        return "Normal Mandibular Position"

# Sample points
S = (1, 2)
N = (2, 3)
A = (3, 4)
B = (4, 5)
CS = (1.5, 2.5)
CE = (2.5, 3.5)

# Calculating the angles
SNA = calculate_angle(S, N, A)
SNB = calculate_angle(S, N, B)
ANB = SNA - SNB
CSA = calculate_angle(CS, CE, A)
CSB = calculate_angle(CS, CE, B)

relationship = classify_skeletal_relationship(ANB)
max_position = maxillary_position(SNA)
mand_position = mandibular_position(SNB)

print(f"SNA Angle: {SNA:.2f} degrees - {max_position}")
print(f"SNB Angle: {SNB:.2f} degrees - {mand_position}")
print(f"ANB Angle: {ANB:.2f} degrees - {relationship}")
print(f"CSA (Cranial to A-point) Angle: {CSA:.2f} degrees")
print(f"CSB (Cranial to B-point) Angle: {CSB:.2f} degrees")
