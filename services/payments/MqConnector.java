package demo.payments;

public class MqConnector {
  public void connect(String queueManager, String channel) {
    System.out.println("Connecting to " + queueManager + "/" + channel);
  }
}
