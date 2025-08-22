import numpy as np

import bottleneck as bn

def recall_at_k_batch(x_pred, heldout_batch, k = 100):
    """
    Hàm này tính toán độ đo Recall@k.

    Args:
        x_pred (numpy.ndarray): Ma trận dự đoán của hệ thống (điểm số).
        heldout_batch (scipy.sparse.csr_matrix): Ma trận dữ liệu thực tế (ground truth).
        k (int): Số lượng mục hàng đầu (top-k) để xem xét.

    Returns:
        numpy.ndarray: Một mảng chứa điểm Recall@k cho mỗi người dùng.
    """
    users_batch = x_pred.shape[0]

    idx = bn.argpartition(-x_pred, k, axis=1)
    binary_x_pred = np.zeros_like(x_pred, dtype = bool)
    binary_x_pred[np.arange(users_batch)[:, np.newaxis], idx[:, :k]] = True
    binary_x_true = (heldout_batch > 0).toarray()

    t = (np.logical_and(binary_x_true, binary_x_pred).sum(axis=1)).astype(np.float32)
    recall_metric = t / np.minimum(k, binary_x_true.sum(axis=1))
    recall_metric[np.isnan(recall_metric)] = 0
    return recall_metric

def ndcg_binary_at_k_batch(x_pred, heldout_batch, k=100):
    """
    Hàm này tính toán độ đo NDCG@k.

    Args:
        x_pred (numpy.ndarray): Ma trận dự đoán của hệ thống (điểm số).
        heldout_batch (scipy.sparse.csr_matrix): Ma trận dữ liệu thực tế (ground truth).
        k (int): Số lượng mục hàng đầu (top-k) để xem xét.

    Returns:
        numpy.ndarray: Một mảng chứa điểm NDCG@k cho mỗi người dùng.
    """
    batch_users = x_pred.shape[0]
    idx_topk_part = bn.argpartition(-x_pred, k, axis=1)
    topk_part = x_pred[np.arange(batch_users)[:, np.newaxis],
                       idx_topk_part[:, :k]]
    idx_part = np.argsort(-topk_part, axis=1)
    idx_topk = idx_topk_part[np.arange(batch_users)[:, np.newaxis], idx_part]
    tp = 1. / np.log2(np.arange(2, k + 2))

    dcg = (heldout_batch[np.arange(batch_users)[:, np.newaxis],
                         idx_topk].toarray() * tp).sum(axis=1)
    idcg = np.array([(tp[:min(n, k)]).sum()
                     for n in heldout_batch.getnnz(axis=1)])
    ndcg_metric = dcg / idcg
    ndcg_metric[np.isnan(ndcg_metric)] = 0
    return ndcg_metric