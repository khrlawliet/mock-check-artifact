from flask import Flask, jsonify
import json

app = Flask(__name__)

# Predefined service versions data
SERVICE_VERSIONS = {
    "user-service": {
        "versions": [
            "1.2.3",
            "1.1.1"
        ]
    },
    "product-service": {
        "versions": [
            "1.1.3",
            "1.0.1"
        ]
    }
}

@app.route('/check-artifact/<service>/<version>', methods=['GET'])
def check_artifact(service, version):
    """
    Check if a service version is available
    
    Args:
        service: The service name (e.g., 'user-service')
        version: The version to check (e.g., '1.2.3')
    
    Returns:
        JSON response with status 'available' or 'unavailable'
    """
    
    # Check if service exists in our predefined data
    if service not in SERVICE_VERSIONS:
        return jsonify({"status": "unavailable"})
    
    # Check if version exists for the service
    if version in SERVICE_VERSIONS[service]["versions"]:
        return jsonify({"status": "available"})
    else:
        return jsonify({"status": "unavailable"})

@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({"status": "healthy"})

@app.route('/', methods=['GET'])
def home():
    """Root endpoint with API information"""
    return jsonify({
        "message": "Service Version Check API",
        "usage": "/check-artifact/<service>/<version>",
        "example": "/check-artifact/user-service/1.2.3"
    })

# For Vercel deployment
if __name__ == '__main__':
    app.run(debug=True)