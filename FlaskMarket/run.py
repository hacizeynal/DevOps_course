from market import app
import os
# docker run -d -p 5002:5000 -e DEBUG=1 --name web_app <image_name>
# Checks if the run.py file has executed directly and not imported
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=os.environ.get("DEBUG") == "1")
