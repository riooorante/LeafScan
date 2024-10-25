def upload_results_to_bucket(bucket_name, destination_path, data):
    print(f"Uploading results to bucket {destination_path}")
    try:
        bucket = storage_client.bucket(bucket_name)
        blob = bucket.blob(destination_path)
        blob.upload_from_string(json.dumps(data), content_type='application/json')
        print(f"Results successfully uploaded to {destination_path}")
    except Exception as e:
        REPORT['error'] = f"Error uploading results to bucket {destination_path}: {e}"
        print(REPORT['error'])
        raise