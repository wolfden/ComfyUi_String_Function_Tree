import re

class StringFunction:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "action": (["append", "replace"], {}),
                "tidy_tags": (["yes", "no"], {}),
            },
            "optional": {
                "text_a": ("STRING", {"multiline": True}),
                "text_b": ("STRING", {"multiline": True}),
                "text_c": ("STRING", {"multiline": True}),
                "text_d": ("STRING", {"multiline": True}),
                "text_e": ("STRING", {"multiline": True}),
                "text_f": ("STRING", {"multiline": True}),
                "text_g": ("STRING", {"multiline": True}),
                "text_h": ("STRING", {"multiline": True}),
                "text_i": ("STRING", {"multiline": True}),
                "text_j": ("STRING", {"multiline": True}),
                "text_k": ("STRING", {"multiline": True}),
                "text_l": ("STRING", {"multiline": True}),
                "text_m": ("STRING", {"multiline": True}),
                "text_n": ("STRING", {"multiline": True}),
                "text_o": ("STRING", {"multiline": True}),
                "text_p": ("STRING", {"multiline": True}),
                "text_q": ("STRING", {"multiline": True}),
                "text_r": ("STRING", {"multiline": True}),
            }
        }

    RETURN_TYPES = ("STRING",)
    FUNCTION = "exec"
    CATEGORY = "utils"
    OUTPUT_NODE = True

    def exec(self, action, tidy_tags, text_a="", text_b="", text_c="", text_d="", text_e="", text_f="", text_g="", text_h="",
             text_i="", text_j="", text_k="", text_l="", text_m="", text_n="", text_o="", text_p="", text_q="", text_r=""):
        # Converted inputs are sent as the string of 'undefined' if not connected
        if text_a == "":
            text_a = ""
        if text_b == "":
            text_b = ""
        if text_c == "":
            text_c = ""
        if text_d == "":
            text_d = ""
        if text_e == "":
            text_e = ""
        if text_f == "":
            text_f = ""
        if text_g == "":
            text_g = ""
        if text_h == "":
            text_h = ""
        if text_i == "":
            text_i = ""
        if text_j == "":
            text_j = ""
        if text_k == "":
            text_k = ""
        if text_l == "":
            text_l = ""
        if text_m == "":
            text_m = ""
        if text_n == "":
            text_n = ""
        if text_o == "":
            text_o = ""
        if text_p == "":
            text_p = ""
        if text_q == "":
            text_q = ""
        if text_r == "":
            text_r = ""

        tidy_tags = tidy_tags == "yes"
        out = ""
        if action == "append":
            out = (", " if tidy_tags else "").join(filter(None, [text_a, text_b, text_c, text_d, text_e, text_f, text_g, text_h, text_i, text_j, text_k, text_l, text_m, text_n, text_o, text_p, text_q, text_r]))
        else:
            if text_r is None:
                text_r = ""
            if text_b.startswith("/") and text_b.endswith("/"):
                regex = text_b[1:-1]
                out = re.sub(regex, text_r, text_a)
            else:
                out = text_a.replace(text_b, text_r)
        if tidy_tags:
            out = out.replace("  ", " ").replace(" ,", ",").replace(",,", ",").replace(",,", ",")
        return {"ui": {"text": (out,)}, "result": (out,)}

NODE_CLASS_MAPPINGS = {
    "StringFunction": StringFunction,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "StringFunction": "String Function Tree",
}
