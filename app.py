from flask import Flask, request, jsonify
import re

app = Flask(__name__)

# ====== YOUR DETAILS (edit these 4 lines) ======
FULL_NAME = "john_doe"     # full name in lowercase with underscore(s)
DOB_DDMMYYYY = "17091999"  # ddmmyyyy
EMAIL = "john@xyz.com"
ROLL_NUMBER = "ABCD123"
# ===============================================

USER_ID = f"{FULL_NAME.lower()}_{DOB_DDMMYYYY}"

def classify_item(s: str):
    """
    Returns one of: 'number', 'alphabet', 'special'
    Number: only digits 0-9 (no signs, no decimals)
    Alphabet: only A-Z or a-z (one or more letters)
    Special: everything else
    """
    if isinstance(s, str) and re.fullmatch(r"\d+", s):
        return "number"
    if isinstance(s, str) and re.fullmatch(r"[A-Za-z]+", s):
        return "alphabet"
    return "special"

def alternating_caps_reverse_concat(chars: str) -> str:
    """
    Reverse the string and apply alternating caps starting with UPPER
    Example: 'ayb' -> reverse 'bya' -> 'ByA'
    """
    out = []
    rev = chars[::-1]
    for i, ch in enumerate(rev):
        out.append(ch.upper() if i % 2 == 0 else ch.lower())
    return "".join(out)

@app.route("/bfhl", methods=["POST"])
def bfhl():
    try:
        payload = request.get_json(force=True, silent=False)
        input_array = payload.get("data", [])
        if not isinstance(input_array, list):
            raise ValueError("`data` must be a JSON array of strings.")

        even_numbers = []
        odd_numbers = []
        alphabets = []
        special_characters = []
        sum_numbers = 0
        alpha_chars_collector = []  # collect all alphabetical characters

        for item in input_array:
            # Ensure everything is treated as string (incoming JSON should already be)
            s = str(item)

            kind = classify_item(s)
            if kind == "number":
                # keep the original string in outputs
                n = int(s)
                if n % 2 == 0:
                    even_numbers.append(s)
                else:
                    odd_numbers.append(s)
                sum_numbers += n
            elif kind == "alphabet":
                alphabets.append(s.upper())  # tokens uppercased
                alpha_chars_collector.append(s)  # for per-character concat later
            else:
                special_characters.append(s)

        # Build alternating caps on ALL alphabetical characters (across tokens)
        all_alpha_chars = "".join(alpha_chars_collector)
        concat_string = alternating_caps_reverse_concat(all_alpha_chars)

        resp = {
            "is_success": True,
            "user_id": USER_ID,
            "email": EMAIL,
            "roll_number": ROLL_NUMBER,
            "odd_numbers": odd_numbers,                 # numbers as strings
            "even_numbers": even_numbers,               # numbers as strings
            "alphabets": alphabets,                     # tokens uppercased
            "special_characters": special_characters,
            "sum": str(sum_numbers),                    # sum as string
            "concat_string": concat_string
        }
        return jsonify(resp), 200

    except Exception as e:
        # On errors, still return user_id and is_success=false
        return jsonify({
            "is_success": False,
            "user_id": USER_ID,
            "message": str(e)
        }), 400

if __name__ == "__main__":
    app.run(debug=True)
