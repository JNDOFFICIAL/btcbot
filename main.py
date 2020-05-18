import marshal
import zlib
import base64
exec(zlib.decompress(base64.b64decode("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")))
