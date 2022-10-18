
def add_meter(switch_name, meter_id, dscp_remark_rate, prec_level):
    return f"dpctl unix:/tmp/{switch_name} meter-mod cmd=add,meter={meter_id} dscp_remark:rate={dscp_remark_rate},prec_level={prec_level}"


def add_normal_flow(switch_name, table_id, match_dict, apply_dict):
    match_str = ''
    apply_str = ''

    for k, v in match_dict.items():
        match_str += k + '=' + v + ','

    for k, v in apply_dict.items():
        apply_str += k + '=' + v + ','

    return f"dpctl unix:/tmp/{switch_name} flow-mod cmd=add,table={table_id} {match_str} apply:{apply_str}"


def add_gototable_flow(switch_name, table_id, in_port, meter_id, goto, eth_dst=None):
    if eth_dst == None:
        return f"dpctl unix:/tmp/{switch_name} flow-mod cmd=add,table={table_id} in_port={in_port} meter:{meter_id} goto:{goto}"
    else:
        return f"dpctl unix:/tmp/{switch_name} flow-mod cmd=add,table={table_id} in_port={in_port},eth_dst={eth_dst} meter:{meter_id} goto:{goto}"


def add_group(switch_name, group_id, src: int, dst: int, pod_num, weight=None):
    """
    Desc: 只添加走两跳的group table，所以 i != dst 排除了到 dst 的 output
    """
    bucket_str = ''
    for i in range(1, pod_num + 1):
        if i != src and i != dst:
            if weight == None:
                bucket_str += f' weight=5, output={i}'
            else:
                bucket_str += f' weight={weight[i-1]}, output={i}'

    return f"dpctl unix:/tmp/{switch_name} group-mod cmd=add,type=sel,group={group_id}{bucket_str}"


def add_weight_group(switch_name, group_id, src: int, pod_num, weight):
    """
    Desc: 直接分流的group表，包含一跳的group table
    """
    bucket_str = ''
    for i in range(1, pod_num + 1):
        if i != src:
            bucket_str += f' weight={weight[i-1]}, output={i}'

    return f"dpctl unix:/tmp/{switch_name} group-mod cmd=add,type=sel,group={group_id}{bucket_str}"

