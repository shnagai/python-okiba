import boto3

ec2 = boto3.client('ec2', region_name='ap-northeast-1')
ec2_instance = ec2.describe_instances(
            Filters=[{'Name':'vpc-id','Values':["vpc-3d53465f"]}]
                )

#list = {'rows': [], 'columns': []}
result = {}

for r in ec2_instance['Reservations']:
    #for i in r['Instances']:
    for i in r['Instances']:
        ##add_result_row(result, {'ip': i['PrivateIpAddress'], 'name': 'hoge'})
        for t in i['Tags']:
            if t['Key'] == 'Name':
                #name = (t['Value'])
                # redashのヘルパーメソッド データ行追加
                add_result_row(result, {'ip': i['PrivateIpAddress'], 'name': t['Value']})

# redashのヘルパーメソッド カラム名指定
add_result_column(result, 'ip', '', 'string')
add_result_column(result, 'name', '', 'string')

# redashヘルパーメソッド 任意のデータソースに対してクエリを実行し結果を取得
execute_query(data_source_name_or_id, query)

# redashヘルパーメソッド redash上のクエリID結果を取得
get_query_result(query_id)
