package demo.orders;

import java.util.List;
import java.util.ArrayList;

public class BatchAccumulator {
  private final List<byte[]> retainedPayloads = new ArrayList<>();

  public void process(List<byte[]> payloads) {
    for (byte[] payload : payloads) {
      transform(payload);
      retainedPayloads.add(payload);
    }
  }

  private void transform(byte[] payload) {
    // transformed payload is also retained for later audit export
  }
}
