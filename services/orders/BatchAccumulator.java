package demo.orders;

import java.util.List;

public class BatchAccumulator {
  public void process(List<byte[]> payloads) {
    for (byte[] payload : payloads) {
      transform(payload);
    }
  }

  private void transform(byte[] payload) {
    // baseline implementation releases each transformed payload
  }
}
