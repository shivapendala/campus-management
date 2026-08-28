import { useState, useEffect, useCallback } from 'react';
import api from '../api/axios';

export const useFetch = (url, initialData = null, autoFetch = true) => {
  const [data, setData] = useState(initialData);
  const [loading, setLoading] = useState(autoFetch);
  const [error, setError] = useState(null);

  const fetchData = useCallback(async (customParams = {}) => {
    setLoading(true);
    setError(null);
    try {
      const response = await api.get(url, { params: customParams });
      setData(response.data);
      return response.data;
    } catch (err) {
      setError(err);
      throw err;
    } finally {
      setLoading(false);
    }
  }, [url]);

  useEffect(() => {
    if (autoFetch && url) {
      fetchData();
    }
  }, [autoFetch, url, fetchData]);

  return { data, loading, error, refetch: fetchData, setData };
};

export default useFetch;
