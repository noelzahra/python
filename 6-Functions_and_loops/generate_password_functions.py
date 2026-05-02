import random, secrets, string

#Function to generate a random password

def create_password(first_name, second_name, num):
        key = random.randint(1, int(num))
        user_name = f"{first_name} {second_name}"
        return f"{user_name} has generated a new password: {key}"

user = create_password("Scott", "Zahra", 10000)
print(user)

#function to generate a more complex password

def generate_token(first_name, second_name):
    token_length = 13
    #Using secrets module: generates cryptographically strong random numbers 
    token = secrets.token_urlsafe(token_length)
    user_name = f"{first_name} {second_name}"
    return f"{user_name} account token:{token}"

token_user = generate_token("Scott", "Zahra")
print(token_user)

#function to generate a randomize key with letters and words

def generate_hash(first_name, second_name):
    hash_length = 13
    #Using string constants
    characters = string.ascii_lowercase + string.ascii_uppercase + string.digits + "!@#$%^&*"
    #Join random characters
    generate_hash_string = ''. join(random.choices(characters, k=hash_length))
    user_name = f"{first_name} {second_name}"
    return f"{user_name} hash key: {generate_hash_string}"

key_user = generate_hash("Scott", "Zahra")
print(key_user)
    
    