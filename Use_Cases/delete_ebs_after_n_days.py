from datetime import datetime, timedelta, timezone
import boto3

ec2Resource = boto3.resource('ec2')

#list of snapshots
#snapshots.filter returns a iterator list of snapshots from aws docs
snapshots = ec2Resource.snapshots.filter(OwnerIds=['self'])

#from that list of snapshots. for each snapshot object lets pull the start_time
for snapshot in snapshots:
    start_time = snapshot.start_time
    delete_time = datetime.now(tz=timezone.utc) - timedelta(days=15)#my idea is to use minutes
    if delete_time > start_time:
        snapshot.delete()
        print('snapshot with id is {} deleted'.format(snapshot.snapshot_id))