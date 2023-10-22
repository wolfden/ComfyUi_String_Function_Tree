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

    def exec(self, action, tidy_tags, text_a=None, text_b=None, text_c=None, text_d=None, text_e=None, text_f=None, text_g=None, text_h=None,
             text_i=None, text_j=None, text_k=None, text_l=None, text_m=None, text_n=None, text_o=None, text_p=None, text_q=None, text_r=None):
        # Check if input is None or "undefined" and replace with an empty string
        text_inputs = [text_a, text_b, text_c, text_d, text_e, text_f, text_g, text_h, text_i, text_j, text_k, text_l, text_m, text_n, text_o, text_p, text_q, text_r]
        text_inputs = ["" if input_value in (None, "undefined") else input_value for input_value in text_inputs]

        tidy_tags = tidy_tags == "yes"
        out = ""
        if action == "append":
            out = (", " if tidy_tags else "").join(filter(None, text_inputs))
        else:
            if text_r is None:
                text_r = ""
            if text_b and text_b.startswith("/") and text_b.endswith("/"):
                regex = text_b[1:-1]
                out = re.sub(regex, text_r, text_a)
            else:
                out = text_a.replace(text_b, text_r)
        if tidy_tags:
            out = out.replace("  ", " ").replace(" ,", ",").replace(",,", ",").replace(",,", ",")
        return {"ui": {"text": (out,)}, "result": (out,)}
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

    def exec(self, action, tidy_tags, text_a=None, text_b=None, text_c=None, text_d=None, text_e=None, text_f=None, text_g=None, text_h=None,
             text_i=None, text_j=None, text_k=None, text_l=None, text_m=None, text_n=None, text_o=None, text_p=None, text_q=None, text_r=None):
        # Check if input is None or "undefined" and replace with an empty string
        text_inputs = [text_a, text_b, text_c, text_d, text_e, text_f, text_g, text_h, text_i, text_j, text_k, text_l, text_m, text_n, text_o, text_p, text_q, text_r]
        text_inputs = ["" if input_value in (None, "undefined") else input_value for input_value in text_inputs]

        tidy_tags = tidy_tags == "yes"
        out = ""
        if action == "append":
            out = (", " if tidy_tags else "").join(filter(None, text_inputs))
        else:
            if text_r is None:
                text_r = ""
            if text_b and text_b.startswith("/") and text_b.endswith("/"):
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
